import time
from progress.bar import Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar

length = 20
# with Bar('Processing', max=length) as bar:
#     for i in range(length):
#         time.sleep(1)
#         bar.next()

# for i in Bar('Processing').iter(range(length)):
#     time.sleep(1)

# from progress.spinner import Spinner
# for i in Spinner(Spinner.__name__).iter(range(10)):
#     time.sleep(1)

from progress.bar import IncrementalBar
with IncrementalBar(IncrementalBar.__name__, max=length, suffix='%(index)d/%(max)d [%(eta_td)s]') as bar:
    for i in bar.iter(range(length)):
        time.sleep(1)

# for bar_cls in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
#     suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
#     bar = bar_cls(bar_cls.__name__, suffix=suffix)
#     for i in bar.iter(range(length)):
#         time.sleep(1)
