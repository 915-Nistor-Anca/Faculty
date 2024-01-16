package com.example.animateapp.data

import android.util.Log
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import com.example.animateapp.ui.movie.toMovie
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


class OnlineMoviesRepository: MoviesRepository {

    private val api: MoviesApi

    init {
        val retrofit = Retrofit.Builder()
            .baseUrl("http://172.20.10.2:5000")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        api = retrofit.create(MoviesApi::class.java)
    }

    override fun getAllMoviesStream(): Flow<List<AnimatedMovie>> = flow {
        emit(api.getAllMovies())
    }

    override fun getMovieStream(id: Int): Flow<AnimatedMovie?> = flow {
        emit(api.getMovie(id))
    }

    override suspend fun insertMovie(animatedMovie: AnimatedMovie) {
        Log.d("INSERTMOVIE", "INSERTED MOVIE IN REPOSITORY: ${animatedMovie}")
        api.insertMovie(animatedMovie)
    }

    override suspend fun deleteMovie(animatedMovie: AnimatedMovie) {
        Log.d("DELETEMOVIE", "DELETED MOVIE IN REPOSITORY: ${animatedMovie}")
        api.deleteMovie(animatedMovie.id)
    }

    override suspend fun updateMovie(animatedMovie: AnimatedMovie) {
        Log.d("UPDATEMOVIE", "UPDATED MOVIE IN REPOSITORY: ${animatedMovie}")
        api.updateMovie(animatedMovie.id, animatedMovie)
    }
}