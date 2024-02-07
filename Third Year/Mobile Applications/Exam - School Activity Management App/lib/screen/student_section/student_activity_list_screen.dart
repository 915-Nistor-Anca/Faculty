import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';
import '../../model/local_database_repository.dart';

class ActivityTypesListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Activity Types'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          return FutureBuilder<List<String>>(
            future: repository.fetchActivitiesTypes(),
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
                      trailing: ElevatedButton(
                        onPressed: () {
                          _requestActivity(context, activityType);
                        },
                        child: Text('Register'),
                      ),
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
    );
  }

  void _requestActivity(BuildContext context, String activityType) async {
    try {
      final String urlServer = "http://10.0.2.2:2407";
      var url = Uri.parse(urlServer + "/activities");
      final response = await http.put(
        url,
        body: jsonEncode({'type': activityType}),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );

      if (response.statusCode == 200) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Successfully registered for $activityType'),
          ),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Failed to register for $activityType'),
          ),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error: $e'),
        ),
      );
    }
  }

}

class ActivitiesInCategoryScreen extends StatelessWidget {
  final String category;

  const ActivitiesInCategoryScreen({Key? key, required this.category}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Activities in $category'),
      ),
      // Fetch and display activities for the selected category
      body: FutureBuilder<List<Map<String, String>>>(
        future: _fetchActivitiesForCategory(category),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (context, index) {
                Map<String, String> activityData = snapshot.data![index];
                return ListTile(
                  title: Text(activityData['name'] ?? ''),
                  subtitle: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('ID: ${activityData['id'] ?? ''}'),
                      Text('Status: ${activityData['status'] ?? ''}'),
                      Text('Type: ${activityData['type'] ?? ''}'),
                    ],
                  ),
                  onTap: () {
                    // Handle tap event
                  },
                );
              },
            );
          }
        },
      ),
    );
  }

  Future<List<Map<String, String>>> _fetchActivitiesForCategory(String category) async {
    // Your HTTP request logic here to fetch activities for the selected category
    return []; // Placeholder, replace it with your actual implementation
  }
}
