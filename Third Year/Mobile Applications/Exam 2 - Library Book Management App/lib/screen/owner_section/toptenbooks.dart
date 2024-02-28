import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/local_database_repository.dart';

class TopBooksByCategoryScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Top Books'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          // Get all available books
          List<Map<String, String>> allBooks = repository.availableBooks;

          // Sort the books by publication year in descending order
          allBooks.sort((a, b) => int.parse(b['year'] ?? '0').compareTo(int.parse(a['year'] ?? '0')));

          // Take the top 10 books
          List<Map<String, String>> topBooks = allBooks.take(10).toList();

          return ListView.builder(
            itemCount: topBooks.length,
            itemBuilder: (context, index) {
              Map<String, String> bookData = topBooks[index];
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
