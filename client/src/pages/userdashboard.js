import { useEffect, useState, useRef } from 'react';
import Bargraph from '../components/bargraph';
import ScatterChart from '../components/scatter';

const UserDashBoard = () => {
  const [clickbaitData, setClickbaitData] = useState();
  const [loading, setLoading] = useState(false);
  const [title, setTitle] = useState();

  useEffect(() => {
    fetch('/api/handleData')
      .then((res) => res.json())
      .then((data) => setClickbaitData(data))
      .catch((err) => console.log(err));
  }, []);

  let today = new Date();
  const options = {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric',
  };

  today = today.toLocaleDateString('en-US', options);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/handleData', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(title),
    });
  };

  return (
    <div className="user-dashboard">
      <div>
        <div className="header">
          <h1 className="title">{today}</h1>
        </div>
        <div className="input-form">
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              onChange={({ target }) => setTitle(target.value)}
              class="searchTerm"
              placeholder="Enter a title here"
            ></input>
            <button type="submit" class="searchButton">
              Enter
            </button>
          </form>
        </div>
        <div className="daily-graphs">
          <ScatterChart clickbaitData={clickbaitData} />
        </div>
      </div>
    </div>
  );
};

export default UserDashBoard;
