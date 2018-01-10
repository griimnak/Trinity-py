import { Component, helpers } from 'trinity-web'

import { required } from 'utils/validation'

export default class Login extends Component {

  initialState = () => ({
    errors: null
  })

  beforeRender() {
    this.addHeadTags(
      { tag: 'link', href: 'pub/__trinity__/vendor/font-awesome/css/font-awesome.min.css' },
      { tag: 'link', href: 'pub/__trinity__/css/main.css' },
      { tag: 'link', href: 'pub/__trinity__/css/animate.min.css' }
    )
  }

  routeWillLeave = () => this.removeHeadTags()

  login = ({ event }) => {
    const data = helpers.form.getFormData(event.target)

    const errors = helpers.form.createValidator(data, {
      username: [required],
      password: [required]
    })

    console.log(data, errors)

    if (errors) {
      this.setState({ errors })
    }

    event.preventDefault()
  }

  events = () => ([
    {
      event: 'submit',
      selector: '#login-form',
      handler: this.login
    }
  ])

  render = ({ state }) => {
    return `
      <div id="content">
        <div class="main-content">
          <div class="main-title">
            Authentication Required
          </div>
        </div>
        <div class="main-content">
          <div class="main">
            <div class="widget-large">
              <div class="title">Login</div>
              <div class="inner">
                Please login below to continue to the admin area.
              </div>
              <div class="inner"><br/>
                ${state.errors ? `
                  <div class="animated pulse infinite alert alert-danger alert-dismissible" role="alert">
                    
                    ${helpers.objectMap(state.errors,
                      (error) => `
                        <a class="close" data-dismiss="alert">
                            <span aria-hidden="true">&times;</span>
                        </a>
                        <strong>Error: </strong>${error}<br />`
                    )}
                  </div>`
                : ''}
                <form id="login-form">
                  <div class="form-group">
                    <p>Username</p>
                    <input name="username" class="form-control" id="username" type="text" aria-describedby="emailHelp" placeholder="Enter username">
                  </div>
                  <div class="form-group">
                    <p>Password</p>
                    <input name="password" class="form-control" id="password" type="password" placeholder="Password">
                  </div>
                  <p>
                    <button name="login-submit" type="submit" class="btn btn-blue" value="Login">Login</button>
                  </p>
                </form>
              </div>
            </div>
            <div class="widget-beware">
              <div class="title">
                <i class="fa fa-exclamation-triangle"> </i>
                Beware
              </div>
              <div class="inner">
                Failed login attempts are recorded and may expose your ip address and/or browser information, continue at your own risk.
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }

}