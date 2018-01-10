import * as Trinity from 'trinity-web'

console.log(Trinity)

export default class Home extends Trinity.Component {

  render = ({ store }) => {
    const { pyinfo, site } = store.get()

    return `
      <div class="container">
        <header>
            <h1>Trinity 3</h1>
            <h4>Installation complete, now what?</h4>
        </header>
        
        <main>
          <section class="features">
            <div class="section-content">
            <h2>Welcome</h2>
              <p>You can access the administration panel: <a href="/login" data-navigate>here</a>.</p> <br />
    
            <h2>Statistics</h2>
              <ul>
                <li>Site name: ${site.name}</li>
                <li>Site desc: ${site.desc}</li>
                <li>Python version: ${pyinfo}</li>
                <li>Port in use by Trinity: ${site.port}</li>
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
  }

}
