import React, { Component } from "react";
import axios from "axios"


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      articles: [],
      
    }
  }
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/articles/")
      .then((res) => this.setState({ articles: articles.data }))
      .catch((err) => console.log(err));
  };

  

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.articles

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Articles</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;

