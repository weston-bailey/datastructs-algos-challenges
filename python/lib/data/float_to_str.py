def float_to_str(f):
  '''
    float_to_str(float) -> str:\n
    creates a string represnetation of scienrific notation.
  '''
  # detect scientific notation
  float_string = repr(f)
  if 'e' in float_string:
    digits, exp = float_string.split('e')
    digits = digits.replace('.', '').replace('-', '')
    exp = int(exp)
    # minus 1 for decimal point in the sci notation
    zero_padding = '0' * (abs(int(exp)) - 1)
    sign = '-' if f < 0 else ''
    if exp > 0:
      float_string = f'{sign}{digits}{zero_padding}.0'
    else:
      float_string = f'{sign}0.{zero_padding}{digits}'
  return float_string