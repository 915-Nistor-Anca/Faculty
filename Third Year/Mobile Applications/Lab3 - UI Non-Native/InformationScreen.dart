import 'package:flutter/material.dart';
import 'AnimatedMovie.dart'; // Import your AnimatedMovie class here

import 'package:flutter/material.dart';
import 'AnimatedMovie.dart'; // Import your AnimatedMovie class here
import 'UpdateScreen.dart'; // Import your UpdateScreen class here
import 'Repository.dart';

class InformationScreen extends StatefulWidget {
  final AnimatedMovie movie;
  final Repository repository;

  InformationScreen({required this.movie, required this.repository});

  @override
  _InformationScreenState createState() => _InformationScreenState();
}
class _InformationScreenState extends State<InformationScreen> {
  late AnimatedMovie _movie;

  @override
  void initState() {
    super.initState();
    _movie = widget.movie;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_movie.name),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Studio: ${_movie.studio}',
              style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8.0),
            Text(
              'Year: ${_movie.year}',
              style: TextStyle(fontSize: 16.0),
            ),
            SizedBox(height: 8.0),
            Text(
              'Description: ${_movie.description}',
              style: TextStyle(fontSize: 16.0),
            ),
            SizedBox(height: 8.0),
            Text(
              'Review: ${_movie.review}',
              style: TextStyle(fontSize: 16.0),
            ),
            SizedBox(height: 20.0),
          ],
        ),
      ),
    );
  }
}
