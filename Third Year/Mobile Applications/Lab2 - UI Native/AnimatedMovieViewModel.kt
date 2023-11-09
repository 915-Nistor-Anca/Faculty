package com.example.animateapp

import androidx.lifecycle.ViewModel
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.State

class AnimatedMovieViewModel : ViewModel() {
    private val animatedMovies: MutableList<AnimatedMovie> = mutableListOf()
    private val animatedMoviesState = mutableStateOf<List<AnimatedMovie>>(emptyList())

    init {
        addAnimatedMovie(AnimatedMovie(0, "Frozen", "Disney", "Two sisters", 2013, "C:\\Users\\ancan\\Desktop\\frozen.jpeg", "Good!"))
        addAnimatedMovie(AnimatedMovie(1, "Toy Story", "Pixar", "Toys come to life", 1995, "def", "Awesome!"))
        addAnimatedMovie(AnimatedMovie(2, "Finding Nemo", "Pixar", "Father clownfish's journey to find his son", 2003, "ghi", "Heartwarming!"))
        addAnimatedMovie(AnimatedMovie(3, "Shrek", "DreamWorks", "Ogre's quest to rescue Princess Fiona", 2001, "jkl", "Hilarious!"))

    }

    fun getNumberOfAnimatedMovies(): Int {
        return animatedMovies.size
    }

    val animated_movies_state: State<List<AnimatedMovie>> get() = animatedMoviesState

    fun getAnimatedMovies(): List<AnimatedMovie> {
         animatedMoviesState.value = animatedMovies
        return animatedMovies
    }

    fun addAnimatedMovie(animated_movie: AnimatedMovie) {
        val i = animatedMovies.indexOfFirst { it.name == animated_movie.name }
        if (i == -1) {
            animatedMovies.add(animated_movie)
            animatedMoviesState.value = animatedMovies
        }
    }

    fun updateAnimatedMovie(new_animated_movie: AnimatedMovie) {
        val i = animatedMovies.indexOfFirst { it.id == new_animated_movie.id }
        if (i >= 0) {
            animatedMovies[i] = new_animated_movie
            animatedMoviesState.value = animatedMovies
        }
    }

    fun deleteAnimatedMovie(id: Int) {
        animatedMovies.removeAll { it.id == id }
        animatedMoviesState.value = animatedMovies
    }

    fun getAnimatedMovieById(id: Int): AnimatedMovie? {
        return animatedMovies.firstOrNull { it.id == id }
    }

    fun getLastAnimatedMovieId(): Int {
        return animatedMovies.last().id
    }


}
