import React, { useEffect, useState } from "react";
import { Button } from "@material-ui/core";
import Movie from "../../components/Movie";
import { api } from "../../services/api";
import "./style.css";
import { Search } from "react-feather";

function Home() {
  const [categories, setCategories] = useState();
  const [movies, setMovies] = useState();
  const [value, setValue] = useState();

  useEffect(() => {
    api.get("categories/all").then((response) => {
      setCategories(response.data);
      console.log(categories[0].nome_categoria);
    });
  }, []);

  useEffect(() => {
    api.get("movies/movie_category/Ação").then((response) => {
      setMovies(response.data);
      console.log(movies);
    });
  }, []);
  function handleChangeCategory(category) {
    api.get(`movies/movie_category/${category}`).then((response) => {
      setMovies(response.data);
    });
  }
  function handleChange(event) {
    const { value } = event.target;
    setValue(value);
  }
  function handleSubmit(event) {
    event.preventDefault();
    console.log(value);
    api.get(`movies/movie_name/${value}`).then((response) => {
      setMovies(response.data);
      console.log(movies);
    });
  }
  return (
    <div className="container">
      <div className="menu">
        <h1 id="title">PurpleTube </h1>
        {categories?.map((element) => (
          <Button
            onClick={() => handleChangeCategory(element.nome_categoria)}
            size="large"
            variant="outlined"
            style={{ marginTop: "1vw", color: "#FFF", width: "15vw" }}
          >
            {element.nome_categoria}
          </Button>
        ))}
      </div>
      <div className="body">
        <div className="menu-top">
          <form className="pesquisa" onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Nome do filme"
              style={{ fontSize: "0.9vw" }}
              onChange={handleChange}
            />
            <button type="submit">
              <Search color="#FFF" />
            </button>
          </form>
          <Button>Login</Button>
        </div>

        <div className="movies">
          {movies?.map((element) => (
            <Movie
              id={element.codigo_filme}
              duration={element.duracao}
              banner={element.baner}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
export default Home;
