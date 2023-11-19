import 'package:flutter/material.dart';
import 'AnimatedMovie.dart';

class UpdateScreen extends StatefulWidget {
  final AnimatedMovie movie;
  final Function(AnimatedMovie) updateMovieCallback;

  UpdateScreen({required this.movie, required this.updateMovieCallback});

  @override
  _UpdateScreenState createState() => _UpdateScreenState();
}

class _UpdateScreenState extends State<UpdateScreen> {
  late TextEditingController nameController;
  late TextEditingController studioController;
  late TextEditingController descriptionController;
  late TextEditingController yearController;
  late TextEditingController reviewController;

  @override
  void initState() {
    super.initState();
    nameController = TextEditingController(text: widget.movie.name);
    studioController = TextEditingController(text: widget.movie.studio);
    descriptionController = TextEditingController(text: widget.movie.description);
    yearController = TextEditingController(text: widget.movie.year.toString());
    reviewController = TextEditingController(text: widget.movie.review);
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
        title: Text('Update Movie'),
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
                final updatedMovie = AnimatedMovie(
                  id: widget.movie.id,
                  name: nameController.text,
                  studio: studioController.text,
                  description: descriptionController.text,
                  year: int.tryParse(yearController.text) ?? 0,
                  review: reviewController.text,
                );

                widget.updateMovieCallback(updatedMovie);

                Navigator.pop(context);
              },
              child: Text('Update Movie'),
            ),
          ],
        ),
      ),
    );
  }
}
