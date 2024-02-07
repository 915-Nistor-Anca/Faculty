import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../model/local_database_repository.dart';
import '../organizer_section/activity_information_screen.dart';

class ParticipationListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Participation List'),
      ),
      body: Consumer<LocalDatabaseRepository>(
        builder: (context, repository, _) {
          Map<String, List<Map<String, String>>> participationsByType = repository.groupParticipationsByType();
          List<String> types = participationsByType.keys.toList();
          return ListView.builder(
            itemCount: types.length,
            itemBuilder: (context, index) {
              String type = types[index];
              List<Map<String, String>> participations = participationsByType[type]!;

              // Calculate the sum of participants for the category
              int sumOfParticipants = participations.fold(0, (sum, activity) {
                int participants = int.tryParse(activity['participants'] ?? '0') ?? 0;
                return sum + participants;
              });

              return ExpansionTile(
                title: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(type),
                    Text('Participants: $sumOfParticipants'),
                  ],
                ),
                children: participations.map((participationData) {
                  return ListTile(
                    title: Text(participationData['name'] ?? ''),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('ID: ${participationData['id']}'),
                        Text('Date: ${participationData['date']}'),
                        Text('Participants: ${participationData['participants']}'),
                      ],
                    ),
                    onTap: () async {
                      // Navigate to the details screen
                      // Example: Navigator.push(context, MaterialPageRoute(builder: (context) => ActivityInformationScreen(activityId: participationData['id'])));
                    },
                  );
                }).toList(),
              );
            },
          );
        },
      ),
    );
  }
}
