import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/book.dart';
import '../../model/local_database_repository.dart';
import '../../websocket.dart';
import 'add_book_screen.dart';
import 'book_information_screen.dart';

class BookListScreen extends StatefulWidget {
  @override
  _BookListScreenState createState() => _BookListScreenState();
}

class _BookListScreenState extends State<BookListScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Book List'),
        actions: [
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AddActivityScreen()),
              );
            },
          ),
        ],
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          List<Map<String, String>> availableActivities =
              repository.availableBooks;
          return ListView.builder(
            itemCount: availableActivities.length,
            itemBuilder: (context, index) {
              Map<String, String> activityData = availableActivities[index];
              return ListTile(
                title: Text(activityData['title'] ?? ''),
                subtitle: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('ID: ${activityData['id']}'),
                    Text('Author: ${activityData['author']}'),
                    Text('Availability: ${activityData['availability']}'),
                  ],
                ),
                onTap: () async {
                  Book? activityDetails = await repository
                      .fetchBookDetails(activityData['id'] ?? '');
                  if (activityDetails != null) {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => ActivityInformationScreen(
                          activity: activityDetails,
                        ),
                      ),
                    );
                  } else {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                          content: Text('Error fetching book details')),
                    );
                  }
                },
              );
            },
          );
        },
      ),
    );
  }
}
