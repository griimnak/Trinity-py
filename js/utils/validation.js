export function required(value) {
  if (!value) {
    return 'This field is required.'
  }
}