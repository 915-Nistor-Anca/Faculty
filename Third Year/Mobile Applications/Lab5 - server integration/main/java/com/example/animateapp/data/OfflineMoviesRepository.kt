package com.example.animateapp.data

import kotlinx.coroutines.flow.Flow

class OfflineMoviesRepository(private val movieDao: MovieDao) : MoviesRepository {
    override fun getAllMoviesStream(): Flow<List<AnimatedMovie>> = movieDao.getAllMovies()

    override fun getMovieStream(id: Int): Flow<AnimatedMovie?> = movieDao.getMovie(id)

    override suspend fun insertMovie(animatedMovie: AnimatedMovie) = movieDao.insert(animatedMovie)

    override suspend fun deleteMovie(animatedMovie: AnimatedMovie) = movieDao.delete(animatedMovie)

    override suspend fun updateMovie(animatedMovie: AnimatedMovie) = movieDao.update(animatedMovie)
}