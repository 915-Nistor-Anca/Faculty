import 'package:flutter/material.dart';
import 'package:proiect_examen/screen/student_section/student_activity_list_screen.dart';
import 'package:proiect_examen/screen/teacher_section/participation_list_screen.dart';
import 'package:provider/provider.dart'; // Import the provider package
import 'package:proiect_examen/screen/organizer_section/activity_list_screen.dart';

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
    ActivityListScreen(),
    ActivityTypesListScreen(),
    ParticipationListScreen(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('School Activity Management App'),
      ),
      body: _widgetOptions.elementAt(_selectedIndex),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.library_books),
            label: 'Organizer Section',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.business),
            label: 'Student Section',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.business),
            label: 'Teacher Section',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.blue,
        onTap: _onItemTapped,
      ),
    );
  }
}
