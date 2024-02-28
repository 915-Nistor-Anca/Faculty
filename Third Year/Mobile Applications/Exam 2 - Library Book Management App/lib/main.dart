import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:retake_ma/screen/owner_section/toptenbooks.dart';
import 'package:retake_ma/screen/registration_section/book_list_screen.dart';
import 'package:retake_ma/screen/report_section/book_genre_list_screen.dart';
import 'package:retake_ma/websocket.dart';
import 'package:provider/provider.dart'; // Import the provider package

import 'model/book.dart';
import 'model/local_database_repository.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider( // Wrap your MaterialApp with MultiProvider
      providers: [
        ChangeNotifierProvider<LocalDatabaseRepository>(
          create: (_) => LocalDatabaseRepository(), // Provide the LocalDatabaseRepository here
        ),
      ],
      child: MaterialApp(
        title: 'Your App Title',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: HomeScreen(),
      ),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  static List<Widget> _widgetOptions = <Widget>[
    BookListScreen(),
    ActivityTypesListScreen()
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  void showAlertDialogForNotification(BuildContext context, Book item) {
    // set up the button
    Widget okButton = ElevatedButton(
      child: const Text("Ok"),
      onPressed: () {
        Navigator.of(context, rootNavigator: true).pop('dialog');
      },
    );

    AlertDialog alert = AlertDialog(
      title: const Text("Notification"),
      actions: [okButton],
      content: Column(mainAxisSize: MainAxisSize.min, children: [
        Text("Id: ${item.id}"),
        const SizedBox(
          height: 10.0,
        ),
        Text("Title: ${item.title}"),
        const SizedBox(
          height: 10.0,
        ),
        Text("Author: ${item.author}"),
        const SizedBox(
          height: 10.0,
        ),
        Text("ISBN: ${item.ISBN}"),
        const SizedBox(
          height: 10.0,
        ),
        Text("Availability: ${item.availability}"),
        const SizedBox(
          height: 10.0,
        ),
        Text("Year: ${item.year}"),
        const SizedBox(
          height: 10.0,
        )
      ]),
    );
    showDialog(
      context: context,
      builder: (BuildContext context) {
        Provider.of<LocalDatabaseRepository>(context, listen: false).fetchBooks();
        Provider.of<LocalDatabaseRepository>(context, listen: false).fetchBooksGenres();
        Provider.of<LocalDatabaseRepository>(context, listen: false).fetchAll();

        return alert;
      },
    );
  }


  @override
  Widget build(BuildContext context) {
    final storage = Provider.of<LocalDatabaseRepository>(context);

    if (storage.connected.value == ConnectionStatus.CONNECTED) {
      storage.checkConnectivity().then((value) {
        if (value == ConnectionStatus.CONNECTED) {
          if (!WebSocketInterface.isListened) {
            // Start listening for WebSocket events
            WebSocketInterface.listen().listen((event) {
              setState(() {
                Book a = Book.fromJson(json.decode(event));
                print("Notification");
                showAlertDialogForNotification(context, a);
              });
            });

            // Set the flag to indicate that we are now listening
            WebSocketInterface.isListened = true;
          }
        }
      });
    }
    return Scaffold(
      appBar: AppBar(
        title: Text('Library Management App'),
      ),
      body: _widgetOptions.elementAt(_selectedIndex),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.library_books),
            label: 'Registration Section',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.business),
            label: 'Report Section',
          ),

        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.blue,
        onTap: _onItemTapped,
      ),
    );
  }
}
