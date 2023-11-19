import 'package:animate_app_nonnative/InformationScreen.dart';
import 'package:flutter/material.dart';
import 'AddScreen.dart';
import 'AnimatedMovie.dart';
import 'Repository.dart';
import 'UpdateScreen.dart';

class ListScreen extends StatefulWidget {
  @override
  _ListScreenState createState() => _ListScreenState();
}

class _ListScreenState extends State<ListScreen> {
  Repository repository = Repository();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Animated Movies'),
      ),
      body: ListView.builder(
        itemCount: repository.getMovies().length,
        itemBuilder: (context, index) {
          final movie = repository.getMovies()[index];
          return Card(
            elevation: 4,
            margin: EdgeInsets.all(8),
            child: ListTile(
              title: Text(movie.name),
              subtitle: Text(movie.studio),
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  IconButton(
                    icon: Icon(Icons.edit),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => UpdateScreen(
                            movie: movie,
                            updateMovieCallback: (updatedMovie) {
                              repository.updateMovie(updatedMovie);
                              setState(() {});
                            },
                          ),
                        ),
                      );
                    },
                  ),
                  IconButton(
                    icon: Icon(Icons.delete),
                    onPressed: () {
                      _confirmDelete(context, movie);
                    },
                  ),
                ],
              ),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => InformationScreen(
                      movie: movie,
                      repository: repository,
                    ),
                  ),
                );
              },
            ),
          );
        },
      ),
      floatingActionButton: Align(
        alignment: Alignment.bottomLeft,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: SizedBox(
            width: MediaQuery.of(context).size.width * 0.35, // Adjust the button width
            child: ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => AddScreen(
                      addMovieCallback: (newMovie) {
                        repository.addMovie(newMovie);
                        setState(() {});
                      },
                    ),
                  ),
                );
              },
              child: Text('Add'),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
                primary: Colors.deepPurple, // Set your desired background color
                padding: EdgeInsets.symmetric(vertical: 16), // Adjust the button's vertical padding
              ),
            ),
          ),
        ),
      ),
    );
  }
  Future<void> _confirmDelete(BuildContext context, AnimatedMovie movie) async {
    return showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Confirm Delete'),
          content: Text('Are you sure you want to delete ${movie.name}?'),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                repository.deleteMovie(movie.id);
                setState(() {});
                Navigator.of(context).pop();
              },
              child: Text('Delete'),
            ),
          ],
        );
      },
    );
  }
}
