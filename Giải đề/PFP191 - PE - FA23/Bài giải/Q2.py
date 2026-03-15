def weighted_average(scores, weights):
    total = sum(s * w for s, w in zip(scores, weights))
    return total/sum(weights)

# print(weighted_average([10, 5, 6, 7], [1, 2, 3, 4]))

def input_and_report():
    while True:
        name = input("Please input student name: ")
        csi_score = float(input("Please input score of CSI105: "))
        mad_score = float(input("Please input score of MAD101: "))
        mae_score = float(input("Please input score of MAE101: "))
        pfp_score = float(input("Please input score of PFP191: "))
        
        scores = [csi_score, mad_score, mae_score, pfp_score]
        weights = [3, 3, 3, 3]
        final_score = weighted_average(scores, weights)
        
        with open("Giải đề/PFP191 - PE - FA23/Bài giải/score_report.txt", "a") as f:
            f.write(f"{name}, {csi_score}, {mad_score}, {mae_score}, {pfp_score}, {final_score}\n")

        check = input("Continue? (y/n): ")
        if check == "n":
            break
        

input_and_report()