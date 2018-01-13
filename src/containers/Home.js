import { Component } from 'trinity-web'

import {
  div,
  header,
  h1,
  h2,
  h4,
  main,
  section,
  p,
  a,
  br,
  ul,
  li
} from 'utils/dom'

export default class Home extends Component {

  render = ({ store }) => {
    const { pyinfo, site } = store.get()

    return (
      div({ className: 'container' })(
        header(
          h1('Trinity 3'),
          h4('Installation complete, now what?')
        ),
        main(
          section({ className: 'features' })(
            div({ className: 'section-content' })(
              h2('Welcome'),
              p(
                'You can access the administration panel: ',
                a({ href: '/login' })('here'),
                br()
              ),

              h2('Statistics'),
              ul(
                li("Site name: ", site.name),
                li("Site desc: ", pyinfo),
                li("Python version: ", pyinfo),
                li("Port in use by Trinity: ", site.port),
              )
            )
          )
        )
      )
    )
  }

}
