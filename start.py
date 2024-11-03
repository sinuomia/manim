from manimlib import *

class UseAxes(Scene):
  def construct(self):
    axes = Axes(x_range=[-10,10,1],y_range=[-10,10,1],)
    axes.add_coordinate_labels(
      font_size=15,
      num_decimal_places=1
    )
    axis_config={
      "include_tip":True,
      "include_numbers": True
    }
    
    curce=axes.get_graph_label(label="y=x^2")
    self.add(axes)