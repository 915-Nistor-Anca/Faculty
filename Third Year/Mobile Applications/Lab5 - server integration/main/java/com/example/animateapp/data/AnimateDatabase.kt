package com.example.animateapp.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [AnimatedMovie::class], version = 1, exportSchema = false)
abstract class AnimateDatabase : RoomDatabase() {

    abstract fun movieDao(): MovieDao

    companion object {
        @Volatile
        private var Instance: AnimateDatabase? = null

        fun getDatabase(context: Context): AnimateDatabase {
            return Instance ?: synchronized(this) {
                Room.databaseBuilder(context, AnimateDatabase::class.java, "animatedmovies2_database")
                    .fallbackToDestructiveMigration()
                    .build()
                    .also { Instance = it }
            }
        }
    }
}