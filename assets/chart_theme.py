"""HSH Report Theme for matplotlib. `from chart_theme import apply, HSH; apply()`."""
import matplotlib as mpl

HSH = dict(
    red='#FF0000', red_chart='#E62601', red_line='#C00000', marker='#4F81BD',
    navy='#002060', navy_chart='#001D5C', blue='#0871D0', pie_blue='#2E75B6', pie_red='#E8000B', pie_gray='#BFBFBF',
    grid='#E5E7EB',
)
PILLARS = ['#D00018', '#0871D0', '#D85A00', '#008E52', '#87329D', '#0098A5', '#D7A000', '#334D64']


def apply():
    mpl.rcParams.update({
        'font.family': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 10, 'font.weight': 'normal',
        'text.color': HSH['navy'], 'axes.labelcolor': HSH['navy'],
        'xtick.color': HSH['navy'], 'ytick.color': HSH['navy'],
        'axes.edgecolor': '#BFC9D9', 'axes.linewidth': 0.75,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.grid': False, 'grid.color': HSH['grid'],
        'axes.prop_cycle': mpl.cycler(color=[HSH['navy_chart'], HSH['red_line'], HSH['blue'], '#D85A00', '#008E52']),
        'legend.frameon': False, 'legend.loc': 'upper center',
        'figure.facecolor': 'white', 'axes.facecolor': 'white',
        'hatch.color': HSH['red_chart'], 'hatch.linewidth': 0.8,
    })


def stacked_growth(ax, cats, base, inc, highlight=None):
    """G2: solid red base + hatched increment + bold navy totals."""
    ax.bar(cats, base, color=HSH['red_chart'], width=0.5, label='Số CH năm hiện tại')
    ax.bar(cats, inc, bottom=base, color='white', edgecolor=HSH['red_chart'], hatch='////', width=0.5, label='Số CH tăng')
    for i, (b, d) in enumerate(zip(base, inc)):
        ax.text(i, b / 2, f'{b}', ha='center', va='center', color=HSH['navy'], fontsize=11)
        ax.text(i, b + d + 6, f'{b + d}', ha='center', va='bottom', color=HSH['navy'], fontsize=12, fontweight='bold')
    if highlight is not None:
        from matplotlib.patches import Ellipse
        t = base[highlight] + inc[highlight]
        ax.add_patch(Ellipse((highlight, t + 14), 0.45, 26, fill=False, color=HSH['red'], lw=1.5))
    ax.legend(ncol=2)
