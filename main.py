import argparse
from math import ceil
import matplotlib.pyplot as plt


def calculate_preemptive_pods_needed(node_capacity, preemptive_pod_resources, scale_up_threshold):
    pods_needed_per_domain = min(
        ceil(node_capacity['cpu'] * scale_up_threshold / preemptive_pod_resources['cpu']),
        ceil(node_capacity['memory'] * scale_up_threshold / preemptive_pod_resources['memory'])
    )
    return pods_needed_per_domain


def calculate_total_preemptive_pods_needed(pods_needed_per_domain, failure_domains):
    return pods_needed_per_domain * failure_domains


def visualize_pods_distribution(pods_needed, failure_domains):
    plt.bar(range(failure_domains), [pods_needed] * failure_domains, color='skyblue')
    plt.xlabel('Failure Domain')
    plt.ylabel('Preemptive Pods Needed')
    plt.title('Preemptive Pods Distribution Across Failure Domains')
    plt.xticks(range(failure_domains), [f"Domain {i+1}" for i in range(failure_domains)])
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='Calculate and visualize preemptive pods distribution for Kubernetes autoscaling.')
    parser.add_argument('--cpu', type=float, default=16, help='Node CPU capacity (default: 16 cores)')
    parser.add_argument('--memory', type=float, default=32, help='Node memory capacity in GB (default: 32 GB)')
    parser.add_argument('--pod_cpu', type=float, default=2, help='Preemptive pod CPU request (default: 0.5 cores)')
    parser.add_argument('--pod_memory', type=float, default=6,
                        help='Preemptive pod memory request in GB (default: 1 GB)')
    parser.add_argument('--scale_up_threshold', type=float, default=0.8,
                        help='Autoscaler scale-up threshold (as a fraction of 1, default: 0.8)')
    parser.add_argument('--failure_domains', type=int, default=3, help='Number of failure domains (default: 3)')
    parser.add_argument('--visualize', default=True, action='store_true',
                        help='Visualize the distribution of preemptive pods (default: off)')

    args = parser.parse_args()

    node_capacity = {'cpu': args.cpu, 'memory': args.memory}
    preemptive_pod_resources = {'cpu': args.pod_cpu, 'memory': args.pod_memory}
    pods_needed_per_domain = calculate_preemptive_pods_needed(node_capacity, preemptive_pod_resources,
                                                              args.scale_up_threshold)
    total_pods_needed = calculate_total_preemptive_pods_needed(pods_needed_per_domain, args.failure_domains)

    print(f"Total preemptive pods needed across all failure domains: {total_pods_needed}")

    if args.visualize:
        visualize_pods_distribution(pods_needed_per_domain, args.failure_domains)


if __name__ == "__main__":
    main()
