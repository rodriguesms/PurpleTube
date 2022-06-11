import './App.css';

import{Route, BrowserRouter as Router, Routes} from 'react-router-dom'
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';


function App() {
  return (
    <Router>
      <Routes>
        <Route exact={true} path="/" element={<Home/>}/>
        <Route exact={true} path="/login" element={<Login/>}/>
        <Route exact={true} path="/register" element={<Register/>} />
      </Routes>
    </Router>
  );
}

export default App;
