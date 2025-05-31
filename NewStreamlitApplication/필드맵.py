import plost

plost.line_chart(
  my_dataframe,
  x='time',
  y=('stock1', 'stock2'),
  pan_zoom='minimap',  # 👈 This is magic!
)