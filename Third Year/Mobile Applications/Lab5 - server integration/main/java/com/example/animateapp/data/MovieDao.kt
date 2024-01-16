package com.example.animateapp.data

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow


@Dao
interface MovieDao {

    @Query("SELECT * from movies ORDER BY name ASC")
    fun getAllMovies(): Flow<List<AnimatedMovie>>

    @Query("SELECT * from movies WHERE id = :id")
    fun getMovie(id: Int): Flow<AnimatedMovie>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun insert(animatedMovie: AnimatedMovie)

    @Update
    suspend fun update(animatedMovie: AnimatedMovie)

    @Delete
    suspend fun delete(animatedMovie: AnimatedMovie)
}