from live_plotter import SeparateProcessLivePlotter, FastLivePlotter
from dataclasses import dataclass
import tyro
from plot_memory_usage.utils import (
    get_cpu_memory_usage,
    get_gpu_memory_usage,
    Units,
    get_num_gpus,
)


@dataclass
class Args:
    units: Units = Units.MB


def main() -> None:
    args: Args = tyro.cli(Args)
    units = args.units

    # Initialize live plotter
    num_gpus = get_num_gpus()
    # plot_names = ["CPU"] + [f"GPU {i}" for i in range(num_gpus)]
    plot_names = [f"CPU {units.name}"] + [
        f"GPU {i} {units.name}" for i in range(num_gpus)
    ]
    ylims = [(0.0, get_cpu_memory_usage().get_total(args.units))] + [
        (0.0, get_gpu_memory_usage(device_id=i).get_total(args.units))
        for i in range(num_gpus)
    ]
    live_plotter = SeparateProcessLivePlotter(
        live_plotter=FastLivePlotter.from_desired_n_plots(
            desired_n_plots=len(plot_names),
            titles=plot_names,
            ylims=ylims,
        ),
        plot_names=plot_names,
    )
    live_plotter.start()

    # Update live plotter
    while True:
        live_plotter.data_dict[f"CPU {units.name}"].append(
            get_cpu_memory_usage().get_used(units)
        )
        for i in range(num_gpus):
            live_plotter.data_dict[f"GPU {i} {units.name}"].append(
                get_gpu_memory_usage(device_id=i).get_used(args.units)
            )

        live_plotter.update()


if __name__ == "__main__":
    main()
