package com.example.animateapp.data

import okhttp3.ResponseBody
import retrofit2.Response
import retrofit2.http.*

interface MoviesApi {
    @GET("/movies")
    suspend fun getAllMovies(): List<AnimatedMovie>

    @GET("/movies/{id}")
    suspend fun getMovie(@Path("id") id: Int): AnimatedMovie?

    @POST("/add_movie")
    @Headers("Content-Type: application/json")
    suspend fun insertMovie(@Body animatedMovie: AnimatedMovie)

    @PUT("/update_movie/{id}")
    @Headers("Content-Type: application/json")
    suspend fun updateMovie(@Path("id") id: Int, @Body animatedMovie: AnimatedMovie)

    @DELETE("/movies/{id}")
    suspend fun deleteMovie(@Path("id") id: Int)

}
