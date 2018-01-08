import { Trinity } from '../src'

import { Home, Dashboard } from './containers'

import { isAuthenticated, isNotAuthenticated } from './routeAuth'

export default function Trinity3() {
  const initialStore =  window.__data ? JSON.parse(window.__data) : {}
  initialStore.lastPage = 'Home'

  const app = new Trinity('app', 'http://localhost:5000', initialStore)

  if (window.__page) {
    app.redirect(window.__page)
  }

  console.log('loading dom shit')

  app.add('/', Home)//isNotAuthenticated
  //app.add('/login')
  app.add('/dashboard', Dashboard)//isAuthenticated

  app.start()
}
