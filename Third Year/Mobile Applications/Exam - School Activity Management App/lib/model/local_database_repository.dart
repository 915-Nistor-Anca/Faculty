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

import 'activity.dart';

enum ConnectionStatus { CONNECTED, CONNECTING, DISCONNECTED }

class LocalDatabaseRepository extends ChangeNotifier {
  List<Map<String, String>> availableActivities = [];
  List<Map<String, String>> availableParticipations = [];
  List<String> activitiesTypes = [];
  List<Activity> activities = [];

  static final String urlServer = "http://10.0.2.2:2407";

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
    await fetchActivities();
    await fetchOrganizerActivities();
    await fetchActivitiesTypes();
    await fetchParticipation();
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

  Future<void> fetchActivities() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/activities");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Activity> activities = jsonDecode(response.body)
            .map<Activity>((t) => Activity.fromJson(t))
            .toList();

        // Extract from activities
        availableActivities = activities.map((car) {
          return {
            'id': car.id.toString(),
            'name': car.name,
            'date': car.date,
            'type': car.type,
            'participants':car.participants.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/activities");
      } else {
        // Return an empty list if response status code is not 200
        availableActivities = [];
      }
    } else {
      log.info("Using existing available activities offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Activity> offlineActivities = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      availableActivities = offlineActivities.map((c) {
        return {
          'id': c.id.toString(),
          'name': c.name,
          'date': c.date,
          'status':c.status,
          'type': c.type,
          'participants':c.participants.toString()
        };
      }).toList();
    }
    notifyListeners();
  }

  Future<void> fetchParticipation() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/participation");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Activity> activities = jsonDecode(response.body)
            .map<Activity>((t) => Activity.fromJson(t))
            .toList();

        // Extract from activities
        availableParticipations = activities.map((car) {
          return {
            'id': car.id.toString(),
            'name': car.name,
            'date': car.date,
            'type': car.type,
            'participants':car.participants.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/participation");
      } else {
        // Return an empty list if response status code is not 200
        availableParticipations = [];
      }
    } else {
      log.info("Using existing available activities offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Activity> offlineActivities = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      availableParticipations = offlineActivities.map((c) {
        return {
          'id': c.id.toString(),
          'name': c.name,
          'date': c.date,
          'status':c.status,
          'type': c.type,
          'participants':c.participants.toString()
        };
      }).toList();
    }
    notifyListeners();
  }

  Map<String, List<Map<String, String>>> groupParticipationsByType() {
    Map<String, List<Map<String, String>>> participationsByCategory = {};

    for (var participationData in availableParticipations) {
      String category = participationData['type'] ?? 'Other';
      if (!participationsByCategory.containsKey(category)) {
        participationsByCategory[category] = [];
      }
      participationsByCategory[category]!.add(participationData);
    }

    return participationsByCategory;
  }

  Future<List<String>> fetchActivitiesTypes() async {
    List<String> activityTypes = [];

    try {
      var url = Uri.parse(urlServer + "/types");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        List<dynamic> jsonResponse = jsonDecode(response.body);

        // Extracting the activity types from the JSON response
        for (var item in jsonResponse) {
          activityTypes.add(item);
        }
      } else {
        print("Failed to fetch activity types. Status code: ${response.statusCode}");

      }
    } catch (e) {
      print("Error fetching activity types: $e");
    }

    return activityTypes;
  }







  Future<List<Map<String, String>>> fetchAvailableActivities() async {
    await checkConnectivity();
    if (connected.value == ConnectionStatus.CONNECTED) {
      connected.value = ConnectionStatus.CONNECTING;
      var url = Uri.parse(urlServer + "/activities");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        connected.value = ConnectionStatus.CONNECTED;
        List<Activity> activities = jsonDecode(response.body)
            .map<Activity>((t) => Activity.fromJson(t))
            .toList();

        // Extract title, author, and genre from cars
        List<Map<String, String>> activitiesDetails = activities.map((c) {
          return {
            'id': c.id.toString(),
            'name': c.name,
            'status':c.status,
            'date': c.date,
            'type': c.type,
            'participants':c.participants.toString()
          };
        }).toList();

        log.info("GET " + urlServer + "/activites");
        return activitiesDetails;
      } else {
        // Return an empty list if response status code is not 200
        return [];
      }
    } else {
      log.info("Using existing available activities offline");
      connected.value = ConnectionStatus.DISCONNECTED;
      List<Activity> offlineActivites = await DatabaseHelper.instance.getAllActivities();

      // Extract from offline cars
      List<Map<String, String>> activityDetails = offlineActivites.map((c) {
        return {
          'id': c.id.toString(),
          'name': c.name,
          'status':c.status,
          'date': c.date,
          'type': c.type,
          'participants': c.participants.toString()
        };
      }).toList();

      return activityDetails;
    }
  }

  Future<void> fetchOrganizerActivities() async {
    try {
      final response = await http.get(Uri.parse('$urlServer/activities'));
      if (response.statusCode == 200) {
        List<Activity> activities = jsonDecode(response.body)
            .map<Activity>((t) => Activity.fromJson(t))
            .toList();
        // Extract from activities
        availableActivities = activities.map((activity) {
          return {
            'id': activity.id.toString(),
            'name': activity.name,
            'date': activity.date,
            'details': activity.details,
            'participants': activity.participants.toString(),
            'status':activity.status,
            'type':activity.type
          };
        }).toList();
        notifyListeners();
      } else {
        // Handle error
      }
    } catch (e) {
      // Handle error
    }
  }


  Future<void> addActivity(Map<String, dynamic> activityDetails) async {
    try {
      final response = await http.post(
        Uri.parse('$urlServer/activity'),
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
  Future<Activity?> fetchActivityDetails(String activityId) async {
    try {
      final response = await http.get(Uri.parse('$urlServer/activity/$activityId'));
      if (response.statusCode == 200) {
        return Activity.fromJson(jsonDecode(response.body));
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
  static const tableNameActivities = 'activities';
  static Database? _database;

  Future<Database?> get database async => _database ??= await _initDatabase();

  Future<Database?> _initDatabase() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    // await deleteDatabase(documentsDirectory.path);
    try {
      String path = join(documentsDirectory.path, 'activities.db');
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
        name TEXT,
        date TEXT,
        details TEXT,
        status TEXT,
        participants INTEGER,
        type TEXT
      )
    ''');
  }

  Map<String, dynamic> toMap(Activity c) {
    return {
      'name': c.name,
      'date': c.date,
      'details': c.details,
      'status': c.status,
      'participants': c.participants,
      'type': c.type,
    };
  }

  Future<int?> insertActivity(Activity c) async {
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
  Future<List<Activity>> getAllActivities() async {
    Database? db = await instance.database;
    List<Map<String, dynamic>> maps = await db!.query(tableNameActivities);
    return List.generate(maps.length, (i) {
      return Activity(
        id: maps[i]['id'],
        name: maps[i]['name'],
        date: maps[i]['date'],
        details: maps[i]['details'],
        status: maps[i]['status'],
        participants: maps[i]['participants'],
        type: maps[i]['type'],
      );
    });
  }

  // Function to update
  Future<void> updateActivity(Activity c) async {
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
