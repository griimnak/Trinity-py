import { Component, createElement } from 'trinity-web'

import { LastPage } from '../components'

export default class Dashboard extends Component {

  routeWillLeave = ({ store }) => {
    // clean up process like remove user from store
    store.set({
      lastPage: {
        url: '/dashboard',
        name: 'Dashboard'
      }
    })
  }

  render = ({ props }) => {
    return createElement(LastPage, props)
  }

}
