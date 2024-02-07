import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/activity.dart';
import '../../model/local_database_repository.dart';

class ReservedBooksScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Reserved Books'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          List<Activity> reservedBooks = repository.activities;
          return ListView.builder(
            itemCount: reservedBooks.length,
            itemBuilder: (context, index) {
              Activity book = reservedBooks[index];
              return ListTile(
                title: Text(book.name),
                subtitle: Text(book.date),
                trailing: IconButton(
                  icon: Icon(Icons.library_books),
                  onPressed: () async {
                    // Borrow the book
                    // Show AlertDialog with borrow status and book details

                  },
                ),
              );
            },
          );
        },
      ),
    );
  }
}
