import 'package:proiect_examen/screen/organizer_section/reserved_books_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/activity.dart';
import '../../model/local_database_repository.dart';
import 'add_activity_screen.dart';
import 'activity_information_screen.dart';

class ActivityListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Activity List'),
        actions: [
        ],
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          List<Map<String, String>> availableCars = repository.availableActivities;
          return ListView.builder(
            itemCount: availableCars.length,
            itemBuilder: (context, index) {
              Map<String, String> activityData = availableCars[index];
              return ListTile(
                title: Text(activityData['name'] ?? ''),
                subtitle: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('ID: ${activityData['id']}'),
                    Text('Date: ${activityData['date']}'),
                    Text('Type: ${activityData['type']}'),
                  ],
                ),
                onTap: () async {
                  // Fetch car details before navigating
                  Activity? activityDetails =
                  await repository.fetchActivityDetails(activityData['id'] ?? '');
                  if (activityDetails != null) {
                    // Navigate to the CarInformationScreen and pass the car details
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) =>
                            ActivityInformationScreen(activity: activityDetails),
                      ),
                    );
                  } else {
                    // Handle error fetching car details
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text('Error fetching activity details')),
                    );
                  }
                },
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => AddCarScreen(
                onActivityAdded: () {
                  // Refresh the car list when a new car is added
                  Provider.of<LocalDatabaseRepository>(context, listen: false)
                      .fetchOrganizerActivities();
                },
              ),
            ),
          );
        },
        tooltip: 'Add Activity',
        child: Icon(Icons.add),
      ),
    );
  }
}
