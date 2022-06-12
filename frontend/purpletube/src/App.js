import './App.css';

import{Route, BrowserRouter as Router, Routes} from 'react-router-dom'
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import MoviePage from './pages/MoviePage';
import TestComment from './pages/TestComments';


function App() {
  return (
    <Router>
      <Routes>
        <Route exact={true} path="/" element={<Home/>}/>
        <Route exact={true} path="/login" element={<Login/>}/>
        <Route exact={true} path="/register" element={<Register/>} />
        <Route exact={true} path="/movie" element={<MoviePage />}/>
        <Route exact={true} path="/test" element={<TestComment/>}/>
      </Routes>
    </Router>
  );
}

export default App;
