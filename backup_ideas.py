class CombinedResults2(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # self.player.get_others_in_group()[0] == self.player.other_player() -> Player Object
        all_players = self.player.in_all_rounds()
        all_others = self.player.get_others_in_group()[0].in_all_rounds()
        others = self.player.get_others_in_group()[0]
        combined_payoff = 0
        correct_answers = 0
        correct_answers_opponent = 0
        correct_answers_team = 0
        combined_payoff_opponent = 0
        combined_payoff_team = 0
        combined_payoff_total = 0
        opponent = self.player.other_player()
        opponent_id = self.player.other_player().id_in_group
        correct_answers = 0
        combined_payoff = 0
        wrong_sums_2 = 0
        total_sums_2 = 0
        wrong_sums_2_opponent = 0
        total_sums_2_opponent = 0
        me = self.player.id_in_group
        titulo = ""
        contrato = 0
        pay_contract = self.player.in_round((Constants.num_rounds/2)+1).pay_contract
        pay_contract_label = ""
        opponent_contract_decision = opponent.in_round((Constants.num_rounds/2)+1).pay_contract
        opponent_contract_decision_label = ""
        if me == 1:
            titulo = "Pagos Etapa 2 - Jugador X"
        else:
            titulo = "Pagos Etapa 2 - Jugador Y"
        # print("Yo " + str(me))
        # print("Oponente " + str(opponent_id))
        # print("Other " + str(others))
        # print("All Others " + str(all_others))
        # print("Group players" + str(self.group.get_players()))
        for player in all_players:
            combined_payoff += player.payoff
            correct_answers += player.correct_answers_2
            correct_answers_opponent += player.other_player().correct_answers_2
            combined_payoff_opponent += player.other_player().pago
            wrong_sums_2 += player.wrong_sums_2
            wrong_sums_2_opponent += player.other_player().wrong_sums_2
            total_sums_2 += player.total_sums_2
            total_sums_2_opponent += player.other_player().total_sums_2

        #Labels:
        if opponent_contract_decision == True:
            opponent_contract_decision_label = "Sí"

        if opponent_contract_decision == False:
            opponent_contract_decision_label = "No"

        if pay_contract == False:
            pay_contract_label = "No"

        if pay_contract == True:
            pay_contract_label = "Sí"

        #VARIABLES DE CONTROL DE PAGOS
        
        
        #No importa el contrato
        pay_for_subtraction = 20
        pay_y_to_x = 8000
        cost_contract_y = 5000
        cost_contract_x = 3000

        #Con CONTRATO
        pay_base_contract_y = 10000
        pay_x_to_y_wrong_subtraction = 30000
        pay_contract_y_first_quote = 8000
        pay_contract_y_second_quote = 7000

        ############ SIN CONTRATO ################

        #X: sin contrato
        if player.id_in_group == 1 and opponent_contract_decision == False:
            self.player.payment_stage_2 = pay_y_to_x - (pay_for_subtraction * total_sums_2)
            contrato = 0

        #Y: sin contrato
        if player.id_in_group == 2 and pay_contract == False:
            self.player.payment_stage_2 = -pay_y_to_x + (100 * correct_answers_opponent )
            contrato = 0

        ############ CON CONTRATO ################

        #X: cumple con sumas
        if player.id_in_group == 1 and opponent_contract_decision == True:
            if correct_answers >= Constants.sumas_obligatorias_contrato:
                self.player.payment_stage_2 = pay_y_to_x - (20 * total_sums_2 )
                contrato = cost_contract_x

        #X: no cumplio con sumas
        if player.id_in_group == 1 and opponent_contract_decision == True:
            if correct_answers < Constants.sumas_obligatorias_contrato: #Falta implementar la pagina de segunda cuota
                self.player.payment_stage_2 = pay_y_to_x - pay_x_to_y_wrong_subtraction + (pay_contract_y_first_quote + pay_contract_y_second_quote)
                contrato = cost_contract_x

        #Y: Jugador X cumple con sumas
        if player.id_in_group == 2 and pay_contract == True:
            if correct_answers_opponent >= Constants.sumas_obligatorias_contrato:
                self.player.payment_stage_2 = -pay_y_to_x + pay_base_contract_y  + (100 * correct_answers_opponent )
                contrato = cost_contract_y

        #Y: Jugador X no cumple con sumas
        if player.id_in_group == 2 and pay_contract == True:
            if correct_answers_opponent < Constants.sumas_obligatorias_contrato:
                self.player.payment_stage_2 = -pay_y_to_x + pay_base_contract_y
                contrato = cost_contract_y

        combined_payoff_total = self.player.payment_stage_2 + self.player.in_round(Constants.num_rounds/2).payment_stage_1
        return {
            'payment_stage_1': self.player.in_round(Constants.num_rounds/2).payment_stage_1,
            'payment_stage_2': self.player.payment_stage_2,
            'combined_payoff_total' : math.trunc(combined_payoff_total),
            'contrato': contrato,
            'titulo': titulo,
            'opponent_contract_decision': opponent_contract_decision_label,
            'pay_contract': pay_contract_label,
            'correct_answers': correct_answers,
            'correct_answers_opponent': correct_answers_opponent,
            'total_sums_2': total_sums_2,
            'total_sums_2_opponent': total_sums_2_opponent
        }
