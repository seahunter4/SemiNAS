import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw_scatter(xdata, ydata, xlim, ylim, xname, yname, path):
    fig = plt.figure()
    plt.xlabel(xname)
    plt.ylabel(yname)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    plt.scatter(xdata, ydata)
    plt.savefig(path)
    plt.clf()


if __name__ == "__main__":
    fig_path = "./figure/"
    with open("grads_data.txt", "r") as f:
        grad_str = f.readline().rstrip()
        label_str = f.readline().rstrip()
        pred_str = f.readline().rstrip()
    grads = grad_str.split(' ')
    labels = label_str.split(' ')
    preds = pred_str.split(' ')
    grads = [float(i) for i in grads]
    labels = [float(i) for i in labels]
    preds = [float(i) for i in preds]
    n = len(grads)
    abs_diffs = [abs(labels[i] - preds[i]) for i in range(n)]
    rel_diffs_pred = [abs((labels[i] - preds[i])/preds[i]) for i in range(n)]
    rel_diffs_lab = [abs((labels[i] - preds[i])/labels[i]) for i in range(n)]

    draw_scatter(grads,
                 rel_diffs_pred,
                 None,
                 (-100,100),
                 'grads',
                 'relative_diffs2pred',
                 fig_path+"grads_rel_diffs2pred.png")

    draw_scatter(grads,
                 rel_diffs_lab,
                 None,
                 None,
                 'grads',
                 'relative_diffs2label',
                 fig_path+"grads_rel_diffs2lab.png")

    draw_scatter(grads,
                 abs_diffs,
                 None,
                 None,
                 'grads',
                 'absolute_diffs',
                 fig_path+"grads_abs_diffs.png")

    draw_scatter(grads,
                 preds,
                 None,
                 None,
                 'grads',
                 'preds',
                 fig_path+"grads_preds.png")

    draw_scatter(grads,
                 labels,
                 None,
                 None,
                 'grads',
                 'labels',
                 fig_path+"grads_labels.png")

    # fig = plt.figure()
    # plt.xlabel('grads')
    # plt.ylabel('relative_diffs2pred')
    # plt.ylim(-100, 100)
    # plt.scatter(grads, rel_diffs_pred)
    # plt.savefig(fig_path + "grads_rel_diffs2pred.png")
    # plt.clf()
    #
    # fig = plt.figure()
    # plt.xlabel('grads')
    # plt.ylabel('relative_diffs2pred')
    # plt.ylim(-100, 100)
    # plt.scatter(grads, rel_diffs_pred)
    # plt.savefig(fig_path + "grads_rel_diffs2pred.png")
    # plt.clf()

