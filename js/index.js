import { Trinity } from 'trinity-web'

import ApiClient from 'trinity-plugin-api'

import { Home, Admin } from './containers'

import { isAuthenticated, isNotAuthenticated } from './routeAuth'

const initialStore =  window.__data ? JSON.parse(window.__data) : {}

console.log(initialStore)

const app = new Trinity('app', initialStore)

app.context('api', new ApiClient('http://localhost:5000'))

if (window.__page) {
  app.redirect(window.__page)
}

app.route('/', Home)
app.route('/login', Admin.Login)

app.start()
