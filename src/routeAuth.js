export const isAuthenticated = {
  redirect: '/', // if is not authenticated redirect
  selector: (state) => !!state.isAuthenticated,
}

export const isNotAuthenticated = {
  redirect: '/dashboard', // if is authenticated redirect
  allowRedirectBack: false,
  selector: (state) => !state.isAuthenticated
}