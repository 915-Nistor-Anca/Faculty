package com.example.animateapp.data

import kotlinx.coroutines.flow.Flow

interface MoviesRepository {

    fun getAllMoviesStream(): Flow<List<AnimatedMovie>>

    fun getMovieStream(id: Int): Flow<AnimatedMovie?>

    suspend fun insertMovie(animatedMovie: AnimatedMovie)

    suspend fun deleteMovie(animatedMovie: AnimatedMovie)

    suspend fun updateMovie(animatedMovie: AnimatedMovie)
}