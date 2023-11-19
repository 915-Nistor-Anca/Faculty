import 'package:flutter/material.dart';
import 'AnimatedMovie.dart'; // Import your AnimatedMovie class here

class AddScreen extends StatefulWidget {
  final Function(AnimatedMovie) addMovieCallback;

  AddScreen({required this.addMovieCallback});

  @override
  _AddScreenState createState() => _AddScreenState();
}

class _AddScreenState extends State<AddScreen> {
  late TextEditingController nameController;
  late TextEditingController studioController;
  late TextEditingController descriptionController;
  late TextEditingController yearController;
  late TextEditingController reviewController;

  @override
  void initState() {
    super.initState();
    nameController = TextEditingController();
    studioController = TextEditingController();
    descriptionController = TextEditingController();
    yearController = TextEditingController();
    reviewController = TextEditingController();
  }

  @override
  void dispose() {
    nameController.dispose();
    studioController.dispose();
    descriptionController.dispose();
    yearController.dispose();
    reviewController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Movie'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: ListView(
          children: [
            TextFormField(
              controller: nameController,
              decoration: InputDecoration(labelText: 'Name'),
            ),
            TextFormField(
              controller: studioController,
              decoration: InputDecoration(labelText: 'Studio'),
            ),
            TextFormField(
              controller: descriptionController,
              decoration: InputDecoration(labelText: 'Description'),
            ),
            TextFormField(
              controller: yearController,
              decoration: InputDecoration(labelText: 'Year'),
              keyboardType: TextInputType.number,
            ),
            TextFormField(
              controller: reviewController,
              decoration: InputDecoration(labelText: 'Review'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                final newMovie = AnimatedMovie(
                  id: DateTime.now().millisecondsSinceEpoch,
                  name: nameController.text,
                  studio: studioController.text,
                  description: descriptionController.text,
                  year: int.tryParse(yearController.text) ?? 0,
                  review: reviewController.text,
                );

                widget.addMovieCallback(newMovie);

                Navigator.pop(context);
              },
              child: Text('Add Movie'),
            ),
          ],
        ),
      ),
    );
  }
}
