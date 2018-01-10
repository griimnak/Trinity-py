import { Container, createElement } from '../../src'

import LastPage from '../components/LastPage'

export default class Home extends Container {

  beforeMount = () => ({

    action: (api) => api.get('http://localhost:5000/'),
    html: `<div>Loading</div>`
  })

  routeWillLeave = ({ store }) => {
    // clean up logic like remove user from store if logout
    store.setState({ lastPage: 'Home' })
  }

  render = ({ props }) => ({
    html: `
    <div class="container">
      <header>
        <h1>Trinity 3</h1>
        <h4>Installation complete, now what?</h4>
      </header>

      <main>
        <section class="features">
          <div class="section-content">
          <h2>Welcome</h2>
            <p>You can access the administration panel: ${createElement(LastPage, { store: props.store })}.</p> <br />

          <h2>Statistics</h2>
            <ul>
              <li>Site name: {{ sitename }}</li>
              <li>Site desc: {{ sitedesc }}</li>
              <li>Python version: {{ pyinfo }}</li>
              <li>Port in use by Trinity: {{ siteport }}</li>
            </ul>
          </div>
        </section>

        <section class="pricing">
          <div class="section-content">
            <h2>Developing with Trinity</h2>
            <p>Trinity uses flask as it's main web module, click below to learn more about flask.</p>
              <center>
                <a href="flask.pocoo.org">
                  <img width="60%" height="60%" src="http://flask.pocoo.org/static/logo/flask.png"/>
                </a>
              </center>
          </div>
        </section>
      </main>
    </div>

  `
  })

}
