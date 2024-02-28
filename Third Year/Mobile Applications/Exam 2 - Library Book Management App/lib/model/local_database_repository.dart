import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:logging/logging.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart';
import 'package:http/http.dart' as http;
import 'package:connectivity/connectivity.dart';
import 'package:web_socket_channel/io.dart';

import 'book.dart';

enum ConnectionStatus { CONNECTED, CONNECTING, DISCONNECTED }

class LocalDatabaseRepository extends ChangeNotifier {
  List<Map<String, String>> availableBooks = [];
  List<Map<String, String>> availableGenres = [];
  List<String> activitiesTypes = [];
  List<Book> activities = [];

  static final String urlServer = "http://10.0.2.2:2419";

  ValueNotifier<ConnectionStatus> connected =
  ValueNotifier(ConnectionStatus.DISCONNECTED);

  static final ValueNotifier<bool> notifier = ValueNotifier(false);
  static final log = Logger('ActivitiesService');

  StreamController<ConnectivityResult> connectivityController =
  StreamController<ConnectivityResult>(sync: true);

  LocalDatabaseRepository() {
    // Initialize repository
    initializeRepository();

    // Set up connectivity listener
    Connectivity().onConnectivityChanged.listen((ConnectivityResult result) {
      if (result == ConnectivityResult.none) {
        connected.value = ConnectionStatus.DISCONNECTED;
      } else {
        connected.value = ConnectionStatus.CONNECTED;
      }
    });
  }


  Future<void> initializeRepository() async {
    await fetchBooks();
    await fetchBooksGenres();
    await fetchAll();
  }

  Future<ConnectionStatus> checkConnectivity() async {
    final ConnectivityResult result = await Connectivity().checkConnectivity();

    if (result == ConnectivityResult.wifi ||
        result == ConnectivityResult.mobile) {
      connected.value = ConnectionStatus.CONNECTED;
    } else {
      connected.value = ConnectionStatus.DISCONNECTED;
    }

    log.info("connected: " + connected.value.toString());
    return connected.value;
  }

  Future<void> fetchBooks() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/all");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Book> activities = jsonDecode(response.body)
            .map<Book>((t) => Book.fromJson(t))
            .toList();

        // Extract from activities
        availableBooks = activities.map((car) {
          return {
            'id': car.id.toString(),
            'title': car.title,
            'author': car.author,
            'genre':car.genre,
            'ISBN': car.ISBN,
            'availability':car.availability,
            'year':car.year.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/all");
      } else {
        // Return an empty list if response status code is not 200
        availableBooks = [];
      }
    } else {
      log.info("Using existing available books offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Book> offlineActivities = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      availableBooks = offlineActivities.map((c) {
        return {
          'id': c.id.toString(),
          'title': c.title,
          'author': c.author,
          'availability':c.availability,
          'ISBN': c.ISBN,
          'genre':c.genre,
          'year':c.year.toString()
        };
      }).toList();
    }
    notifyListeners();
  }

  Future<void> fetchAll() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/all");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Book> activities = jsonDecode(response.body)
            .map<Book>((t) => Book.fromJson(t))
            .toList();

        // Extract from activities
        availableGenres = activities.map((car) {
          return {
            'id': car.id.toString(),
            'title': car.title,
            'author': car.author,
            'genre':car.genre,
            'ISBN': car.ISBN,
            'availability': car.availability,
            'year':car.year.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/all");
      } else {
        // Return an empty list if response status code is not 200
        availableGenres = [];
      }
    } else {
      log.info("Using existing available books offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Book> offlineActivities = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      availableGenres = offlineActivities.map((c) {
        return {
          'id': c.id.toString(),
          'title': c.title,
          'author': c.author,
          'availability':c.availability,
          'ISBN': c.ISBN,
          'genre':c.genre,
          'year':c.year.toString()
        };
      }).toList();
    }
    notifyListeners();
  }

  Map<String, List<Map<String, String>>> groupParticipationsByType() {
    Map<String, List<Map<String, String>>> participationsByCategory = {};

    for (var participationData in availableGenres) {
      String category = participationData['genre'] ?? 'Other';
      if (!participationsByCategory.containsKey(category)) {
        participationsByCategory[category] = [];
      }
      participationsByCategory[category]!.add(participationData);
    }

    return participationsByCategory;
  }

  Future<List<Map<String, String>>> fetchAvailableActivitiesByGenre(String genre) async {
    List<Map<String, String>> activities = [];
    // Implement logic to fetch activities by genre from your local database or server
    // For example, if you are using a local SQLite database:
    try {
      List<Book> books = await DatabaseHelper.instance.getActivitiesByGenre(genre);
      activities = books.map((book) {
        return {
          'id': book.id.toString(),
          'title': book.title,
          'author': book.author,
          'genre': book.genre,
          'availability': book.availability,
          'year': book.year.toString(),
          'ISBN': book.ISBN,
        };
      }).toList();
    } catch (e) {
      // Handle error
      print('Error fetching activities by genre: $e');
    }
    return activities;
  }



  Future<List<String>> fetchBooksGenres() async {
    List<String> activityTypes = [];

    try {
      var url = Uri.parse(urlServer + "/genres");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        List<dynamic> jsonResponse = jsonDecode(response.body);

        // Extracting the activity types from the JSON response
        for (var item in jsonResponse) {
          activityTypes.add(item);
        }
      } else {
        print("Failed to fetch genres. Status code: ${response.statusCode}");

      }
    } catch (e) {
      print("Error fetching genres: $e");
    }

    return activityTypes;
  }







  Future<List<Map<String, String>>> fetchAvailableActivities() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/all");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Book> activities = jsonDecode(response.body)
            .map<Book>((t) => Book.fromJson(t))
            .toList();

        // Extract title, author, and genre from cars
        List<Map<String, String>> activitiesDetails = activities.map((c) {
          return {
            'id': c.id.toString(),
            'title': c.title,
            'availability':c.availability,
            'author': c.author,
            'ISBN': c.ISBN,
            'year':c.year.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/all");
        return activitiesDetails;
      } else {
        // Return an empty list if response status code is not 200
        return [];
      }
    } else {
      log.info("Using existing available books offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Book> offlineActivites = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      List<Map<String, String>> activityDetails = offlineActivites.map((c) {
        return {
          'id': c.id.toString(),
          'title': c.title,
          'availability':c.availability,
          'author': c.author,
          'ISBN': c.ISBN,
          'year': c.year.toString()
        };
      }).toList();

      return activityDetails;
    }
  }


  Future<void> addBook(Map<String, dynamic> activityDetails) async {
    try {
      final response = await http.post(
        Uri.parse('$urlServer/book'),
        body: jsonEncode(activityDetails),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );

      if (response.statusCode == 200) {
        // Update local data
        await fetchAvailableActivities();
      } else {
        // Handle error
      }
    } catch (e) {
      // Handle error
    }
  }

  Future<void> deleteBook(String activityId) async {
    try {
      // Delete the activity from the local database
      await DatabaseHelper.instance.deleteActivity(int.parse(activityId));
      // Refresh the activity list after deletion
      await fetchBooks();
    } catch (e) {
      // Handle error
      print('Error deleting book: $e');
    }
  }

  Future<Book?> fetchBookDetails(String activityId) async {
    try {
      final response = await http.get(Uri.parse('$urlServer/book/$activityId'));
      if (response.statusCode == 200) {
        return Book.fromJson(jsonDecode(response.body));
      } else {
        // Handle error
        return null;
      }
    } catch (e) {
      // Handle error
      return null;
    }
  }


}

class DatabaseHelper {
  DatabaseHelper._privateConstructor();

  static final DatabaseHelper instance = DatabaseHelper._privateConstructor();
  static const tableNameActivities = 'books3';
  static Database? _database;

  Future<Database?> get database async => _database ??= await _initDatabase();

  Future<Database?> _initDatabase() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    // await deleteDatabase(documentsDirectory.path);
    try {
      String path = join(documentsDirectory.path, 'books3.db');
      return await openDatabase(path, version: 1, onCreate: _onCreate);
    } catch (e) {
      print(e.toString());
    }
    return null;
  }

  Future<void> _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE $tableNameActivities(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        genre TEXT,
        availability TEXT,
        year INTEGER,
        ISBN TEXT
      )
    ''');
  }

  // Inside DatabaseHelper class

  Future<List<Book>> getActivitiesByGenre(String genre) async {
    Database? db = await instance.database;
    List<Map<String, dynamic>> maps = await db!.query(
      tableNameActivities,
      where: 'genre = ?',
      whereArgs: [genre],
    );
    return List.generate(maps.length, (i) {
      return Book(
        id: maps[i]['id'],
        title: maps[i]['title'],
        author: maps[i]['author'],
        genre: maps[i]['genre'],
        availability: maps[i]['availability'],
        year: maps[i]['year'],
        ISBN: maps[i]['ISBN'],
      );
    });
  }


  Map<String, dynamic> toMap(Book c) {
    return {
      'title': c.title,
      'author': c.author,
      'genre': c.genre,
      'availability': c.availability,
      'year': c.year,
      'ISBN': c.ISBN,
    };
  }

  Future<int?> insertActivity(Book c) async {
    Database? db = await instance.database;
    try {
      int? id = await db?.insert(tableNameActivities, toMap(c));
      return id; // Return the auto-generated ID
    } catch (e) {
      print("Error inserting item: $e");
      return null;
    }
  }

  // Function to retrieve all cars
  Future<List<Book>> getAllActivities() async {
    Database? db = await instance.database;
    List<Map<String, dynamic>> maps = await db!.query(tableNameActivities);
    return List.generate(maps.length, (i) {
      return Book(
        id: maps[i]['id'],
        title: maps[i]['title'],
        author: maps[i]['author'],
        genre: maps[i]['genre'],
        availability: maps[i]['availability'],
        year: maps[i]['year'],
        ISBN: maps[i]['ISBN'],
      );
    });
  }

  // Function to update
  Future<void> updateActivity(Book c) async {
    Database? db = await instance.database;
    await db?.update(
      tableNameActivities,
      c.toMap(),
      where: 'id = ?',
      whereArgs: [c.id],
    );
  }

  // Function to delete
  Future<void> deleteActivity(int id) async {
    Database? db = await instance.database;
    await db?.delete(
      tableNameActivities,
      where: 'id = ?',
      whereArgs: [id],
    );
  }
}
