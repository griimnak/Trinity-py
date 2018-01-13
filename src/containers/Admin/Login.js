import { Component, helpers } from 'trinity-web'

import { link, a, div, strong, form, p, input, button, i, br, fragment, span } from 'utils/dom'
import { required } from 'utils/validation'

export default class Login extends Component {

  initialState = () => ({
    errors: null
  })

  beforeRender() {
    helpers.dom.removeHeadTag('App')

    this.addHeadTags(
      link({ href: 'pub/assets/vendor/font-awesome/css/font-awesome.min.css' }),
      link({ href: 'pub/assets/css/main.css' }),
      link({ href: 'pub/assets/css/animate.min.css'})
    )
  }

  routeWillLeave = () => this.removeHeadTags()

  login = (event) => {
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

  render = ({ state }) => {
    return (
      div({ id: 'context' })(
        div({ className: 'main-content' })(
          div({ className: 'main-title' })(
            'Authentication Required'
          )
        ),
        div({ className: 'main-content' })(
          div({ className: 'main' })(
            div({ className: 'widget-large' })(
              div({ className: 'title' })(
                'Login'
              ),
              div({ className: 'inner' })(
                'Please login below to continue to the admin area.'
              ),
              div({ className: 'inner' })(
                br(),
                state.errors && (
                  div({ className: 'animated pulse infinite alert alert-danger alert-dismissible', role: 'alert' })(
                    helpers.objectMap(state.errors,
                      (error) => fragment(
                        a({ className: 'close' })(
                          span('x')
                        ),
                        strong('Error: '), error,
                        br()
                      )
                    )
                  )
                ),
                form({ onSubmit: this.login })(
                  div({ className: 'form-group' })(
                    p('Username'),
                    input({
                      name: 'username',
                      className: 'form-control',
                      placeholder: 'Enter username'
                    })()
                  ),
                  div({ className: 'form-group' })(
                    p('Password'),
                    input({
                      name: 'username',
                      type: 'password',
                      className: 'form-control',
                      placeholder: 'Enter password'
                    })()
                  ),
                  p(
                    button({ type: 'submit', className: 'btn btn-blue' })(
                      'Login'
                    )
                  )
                )
              )
            ),
            div({ className: 'widget-beware' })(
              div({ className: 'title' })(
                i({ className: 'fa fa-exclamation-triangle' })()
              ),
              div({ className: 'inner' })(
                'Failed login attempts are recorded and may expose your ip address and/or browser information, continue at your own risk.'
              )
            )
          )
        )
      )
    )
  }

}