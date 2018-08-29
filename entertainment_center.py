import media
import fresh_tomatoes

#Creating instance of Movie() type for Iron Man
iron_man = media.Movie("Iron Man",
                       "Iron Man is a 2008 American superhero film based on the Marvel Comics character of the same name",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=W7yOdog7Dxg")

#Creating instance of Movie() type for Iron Man 2
iron_man2 = media.Movie("Iron Man 2",
                        "Iron Man 2 Tony Stark is pictured center "
                        "wearing a smart suit, against a black background,"
                        " behind him are the Iron Man red and gold armor, and "
                        "the Iron Man silver armor. His friends, Rhodes, Pepper, "
                        "are beside him and below against a fireball appears Ivan Vanko "
                        "armed with his energy whip weapons. Theatrical release poster Directed "
                        "by Jon Favreau Produced by Kevin Feige Screenplay by Justin Theroux Based "
                        "on Iron Man by Stan Lee Larry Lieber Don Heck Jack Kirby Starring "
                        "Robert Downey Jr. Gwyneth Paltrow Don Cheadle Scarlett Johansson Sam "
                        "Rockwell Mickey Rourke Samuel L. Jackson Music by John Debney Cinematography"
                        "Matthew Libatique Edited by Dan Lebental Richard Pearson Production company "
                        "Marvel Studios Fairview Entertainment Distributed by Paramount Pictures "
                        "Release date April 26, 2010 (El Capitan Theatre) May 7, 2010 (United States) "
                        "Running time 125 minutes[4] Country United States Language English Budget $200 "
                        "million[5][6][7] Box office $623.9 million[6] Iron Man 2 is a 2010 American "
                        "superhero film based on the Marvel Comics character Iron Man, produced by Marvel "
                        "Studios and distributed by Paramount Pictures. It is the sequel to 2008's Iron Man.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=BoohRoVA9WQ")

#Creating instance of Movie() type for Avengers
avenger = media.Movie("Avengers",
                      "The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero "
                      "team of the same name, produced by Marvel Studios and distributed by Walt Disney "
                      "Studios Motion Pictures.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                      "https://www.youtube.com/watch?v=eOrNdBpGMv8")
                                                                                
#Creating instance of Movie() type for Iron Man 3
iron_man3 = media.Movie("Iron Man 3",
                        "Iron Man 3 (stylized onscreen as Iron Man Three) is a \
                        2013 American superhero film based on the Marvel Comics character Iron Man, produced by "
                        "Marvel Studios and distributed by Walt Disney Studios Motion Pictures.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

#Creating instance of Movie() type for Avengers: Age Of Ultron
age_of_ultron = media.Movie("Avengers: Age Of Ultron",
                            "Avengers: Age of Ultron is a 2015 American superhero film based on the Marvel Comics "
                            "superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney "
                            "Studios Motion Pictures. It is the sequel to 2012's The Avengers.",
                            "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",
                            "https://www.youtube.com/watch?v=tmeOjFno6Do")

#Creating instance of Movie() type for Avengers: Infinity War
infinity_war = media.Movie("Avengers: Infinity War",
                           "Endgame with Thanos",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                           "https://www.youtube.com/watch?v=QwievZ1Tx-8")

#Set the movies that will be passed to freshtomatoes.py
movies = [iron_man,
          iron_man2,
          avenger,
          iron_man3,
          age_of_ultron,
          infinity_war]

#Calling function of freshtomatoes.py for creating the webpage
fresh_tomatoes.open_movies_page(movies)
