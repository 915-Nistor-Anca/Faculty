package com.example.animateapp.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "movies")
data class AnimatedMovie(
    @PrimaryKey(autoGenerate = true)
    val id: Int = 0,
    val name: String,
    val studio: String,
    val year: Int,
    val review: String
)