import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/activity.dart';
import '../../model/local_database_repository.dart';

class ActivityInformationScreen extends StatelessWidget {
  final Activity activity;

  ActivityInformationScreen({required this.activity});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Activity Information'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Id: ${activity.id}'),
            Text('Name: ${activity.name}'),
            Text('Date: ${activity.date}'),
            Text('Details: ${activity.details}'),
            Text('Status: ${activity.status}'),
            Text('Participants: ${activity.participants}'),
            Text('Type: ${activity.type}'),
            SizedBox(height: 20),
          ],
        ),
      ),
    );
  }
}
