export interface Event {
    id: string,
    name: string
    date: Date,
    location: string,
    requirements: string,
    budget_upper: number,
    budget_lower: number,
    status: string,
    reviewer_summery: string | null
}

export interface AddEventFormProps {
    onClose: () => void
}