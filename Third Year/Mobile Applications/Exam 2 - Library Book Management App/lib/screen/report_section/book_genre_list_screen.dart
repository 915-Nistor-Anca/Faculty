import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';
import '../../model/local_database_repository.dart';
import '../owner_section/toptenbooks.dart';

class ActivityTypesListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Book Types'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          return FutureBuilder<List<String>>(
            future: repository.fetchBooksGenres(),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Error: ${snapshot.error}'));
              } else {
                List<String>? activityTypes = snapshot.data;
                if (activityTypes == null) {
                  // Handle case when activity types are not fetched yet
                  return Center(child: CircularProgressIndicator());
                }

                return ListView.builder(
                  itemCount: activityTypes.length,
                  itemBuilder: (context, index) {
                    String activityType = activityTypes[index];
                    return ListTile(
                      title: Text(activityType),
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => ActivitiesInCategoryScreen(
                              category: activityType,
                            ),
                          ),
                        );
                      },
                    );
                  },
                );
              }
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Navigate to the TopBooksByCategoryScreen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => TopBooksByCategoryScreen(),
            ),
          );
        },
        child: Icon(Icons.arrow_forward),
      ),
    );
  }
}


class ActivitiesInCategoryScreen extends StatelessWidget {
  final String category;

  const ActivitiesInCategoryScreen({Key? key, required this.category})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Books in $category'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          // Filter available books by category
          List<Map<String, String>> filteredBooks = repository.availableBooks
              .where((book) => book['genre'] == category)
              .toList();

          return ListView.builder(
            itemCount: filteredBooks.length,
            itemBuilder: (context, index) {
              Map<String, String> bookData = filteredBooks[index];
              return ListTile(
                title: Text(bookData['title'] ?? ''),
                subtitle: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('Author: ${bookData['author'] ?? ''}'),
                    Text('Availability: ${bookData['availability'] ?? ''}'),
                  ],
                ),
              );
            },
          );
        },
      ),
    );
  }
}



