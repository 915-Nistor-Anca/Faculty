import 'AnimatedMovie.dart';

class Repository{
  final List<AnimatedMovie> _movies = [];

  Repository() {
    addMovie(
      AnimatedMovie(
        id: 0,
        name: "Frozen",
        studio: "Disney",
        description: "Two sisters",
        year: 2013,
        review: "Good!",
      ),
    );

    addMovie(
      AnimatedMovie(
        id: 1,
        name: "Toy Story",
        studio: "Pixar",
        description: "Toys come to life",
        year: 1995,
        review: "Awesome!",
      ),
    );

    addMovie(
      AnimatedMovie(
        id: 2,
        name: "Finding Nemo",
        studio: "Pixar",
        description: "Father clownfish's journey to find his son",
        year: 2003,
        review: "Heartwarming!",
      ),
    );

    addMovie(
      AnimatedMovie(
        id: 3,
        name: "Shrek",
        studio: "DreamWorks",
        description: "Ogre's quest to rescue Princess Fiona",
        year: 2001,
        review: "Hilarious!",
      ),
    );

  }

  List<AnimatedMovie> getMovies(){
    return _movies;
  }

  AnimatedMovie getMovieById(int id) {
    return _movies.firstWhere((movie) => movie.id == id);
  }

  void addMovie(AnimatedMovie movie) {
    _movies.add(movie);
  }

  void updateMovie(AnimatedMovie movie) {
    final index = _movies.indexWhere((m) => m.id == movie.id);
    if (index != -1) {
      _movies[index] = movie;
    }
  }

  void deleteMovie(int id) {
    _movies.removeWhere((movie) => movie.id == id);
  }
}