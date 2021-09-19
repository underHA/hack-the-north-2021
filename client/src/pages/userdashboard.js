import { useEffect, useState, useRef } from 'react';
import Bargraph from '../components/bargraph';
import ScatterChart from '../components/scatter';
import loadingGif from '../images/loading.gif';

const UserDashBoard = () => {
  const [clickbaitData, setClickbaitData] = useState();
  const [loading, setLoading] = useState(false);
  const [title, setTitle] = useState();

  useEffect(() => {
    if (loading) {
      fetch('/api/handleData')
        .then((res) => res.json())
        .then((data) => setClickbaitData(data))
        .catch((err) => console.log(err));
      setLoading(false);
    }
  }, [loading]);

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
    fetch('/api/handleData', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(title),
    });
    setLoading(true);
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
              placeholder="Enter any title to see if it's clickbait!"
            ></input>
            <button type="submit" class="searchButton">
              Enter
            </button>
          </form>
        </div>
        {loading ? (
          <img src={loadingGif} />
        ) : (
          <div>
            <div className="clickbait-analysis">
              {clickbaitData && (
                <p>
                  The article you clicked on is {clickbaitData.clickbait}%
                  clickbait.
                </p>
              )}
              {clickbaitData && (
                <p>Scroll to the graph below to see details. </p>
              )}
            </div>
            <br />
            <br />
            <br />
            <div className="daily-graphs">
              {clickbaitData && (
                <ScatterChart clickbaitData={clickbaitData.coordinates} />
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default UserDashBoard;
