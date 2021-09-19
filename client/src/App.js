import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Navbar from './components/navbar';
import Homepage from './pages/homepage';
import UserDashBoard from './pages/userdashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
      </div>
      <Switch>
        <Route exact path="/">
          <Homepage />
        </Route>
        <Route path="/dashboard">
          <UserDashBoard />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
