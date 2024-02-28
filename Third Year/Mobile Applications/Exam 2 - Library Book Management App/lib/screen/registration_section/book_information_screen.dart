import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/book.dart';
import '../../model/local_database_repository.dart';
import '../../websocket.dart';

class ActivityInformationScreen extends StatefulWidget {
  final Book activity;

  ActivityInformationScreen({required this.activity});

  @override
  _ActivityInformationScreenState createState() =>
      _ActivityInformationScreenState();
}

class _ActivityInformationScreenState extends State<ActivityInformationScreen> {
  late Book _activity;

  @override
  void initState() {
    super.initState();
    _activity = widget.activity;
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: Text('Book Information'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Id: ${_activity.id}'),
            Text('Title: ${_activity.title}'),
            Text('Author: ${_activity.author}'),
            Text('Genre: ${_activity.genre}'),
            Text('Availability: ${_activity.availability}'),
            Text('Year: ${_activity.year}'),
            Text('ISBN: ${_activity.ISBN}'),
            SizedBox(height: 20),
          ],
        ),
      ),
    );
  }
}
